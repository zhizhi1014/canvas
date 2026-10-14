# -*- coding: utf-8 -*-
r"""metrics.py — Canvas evaluation toolkit
=================================================================
Standard:  Precision, Recall, F1, IoU, FAR, OA
Physics :  RCQ, TRR, MTV, EAS   (one-to-one with the module update rules)
Cross  :  TCI                   (thermal contribution)

Usage:
    from metrics import standard_metrics, rcq, trr, mtv, eas, tci
"""
import numpy as np
import torch
import cv2


# ------------------------- standard -------------------------
def standard_metrics(pred, gt):
    """pred, gt: {0,1} uint8 HxW  ->  dict of %, and FAR=FP/(FP+TN)."""
    pred = np.asarray(pred).astype(bool)
    gt = np.asarray(gt).astype(bool)
    tp = int((pred & gt).sum()); fp = int((pred & ~gt).sum())
    fn = int((~pred & gt).sum()); tn = int((~pred & ~gt).sum())
    prec = tp / max(tp + fp, 1)
    rec = tp / max(tp + fn, 1)
    f1 = 2 * prec * rec / max(prec + rec, 1e-8)
    iou = tp / max(tp + fp + fn, 1)
    far = fp / max(fp + tn, 1)
    oa = (tp + tn) / max(tp + fp + fn + tn, 1)
    return {'Precision': prec, 'Recall': rec, 'F1': f1, 'IoU': iou, 'FAR': far, 'OA': oa}


# ------------------------- physics -------------------------
def rcq(F_align, F_ref):
    """Radiometric Compensation Quality (CMRA). Lower is better.
    F_align, F_ref: (B,C,H,W) tensors -> (1/(N*C)) * ||F_align - F_ref||_1."""
    d = (F_align - F_ref).abs()
    return float(d.sum() / (d.numel() / d.shape[0]))


def trr(F_ter, F_ref, eps=1e-8):
    """Terrain Response Ratio (TGM). Higher = terrain branch engaged."""
    n_ter = F_ter.flatten(1).norm(dim=1).mean()
    n_ref = F_ref.flatten(1).norm(dim=1).mean()
    return float(n_ter / (n_ref + eps))


def _boundary_band(gt, delta):
    """delta-pixel band around the GT change contour (bool HxW)."""
    gt = (np.asarray(gt) > 0).astype(np.uint8)
    k = np.ones((2 * delta + 1, 2 * delta + 1), np.uint8)
    return cv2.dilate(gt, k) - cv2.erode(gt, k) > 0


def mtv(M, gt, delta=3):
    """Mean Total Variation of M outside the GT boundary band (SAVR). Lower = smoother."""
    M = np.asarray(M, np.float32)
    gx = cv2.Sobel(M, cv2.CV_32F, 1, 0, 3); gy = cv2.Sobel(M, cv2.CV_32F, 0, 1, 3)
    outside = ~_boundary_band(gt, delta)
    tv = np.abs(gx) + np.abs(gy)
    return float(tv[outside].mean())


def eas(pred, gt, delta=3):
    """Edge Alignment Score (SAVR): F1 within a delta-pixel band of the GT contour."""
    band = _boundary_band(gt, delta)
    p = (np.asarray(pred) > 0) & band
    g = (np.asarray(gt) > 0) & band
    tp = int((p & g).sum()); fp = int((p & ~g).sum()); fn = int((~p & g).sum())
    return 2 * tp / max(2 * tp + fp + fn, 1)


# ------------------------- cross-modal -------------------------
def tci(f1_rgbtir, f1_rgb):
    """Thermal Contribution Index: change-class F1(RGB-TIR) - F1(RGB)."""
    return float(f1_rgbtir - f1_rgb)
