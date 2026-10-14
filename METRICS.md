# Evaluation Metrics

We adopt five standard quantitative metrics, four physics-grounded indices (each mapped
one-to-one to an update rule of the method), and two cross-modal indices that quantify the
value of the thermal modality. An easy-to-use toolkit implementing these metrics is
open-sourced on our [GitHub Repository](https://github.com/PRIM0829/PRIM).

---

## 1. Standard Metrics

| Metric | Definition |
| --- | --- |
| **Precision (Pre.)** | proportion of detected change pixels that are true changes (suppresses false alarms) |
| **Recall (Rec.)** | proportion of true change pixels that are detected |
| **F1** | harmonic mean of Precision and Recall |
| **IoU** | spatial overlap between prediction and ground truth |
| **OA** | Overall Accuracy — fraction of correctly classified pixels |
| **FAR** | False Alarm Rate, `FP / (FP + TN)` (reported once negative samples are included) |

---

## 2. Physics-Grounded Indices

### Radiometric Compensation Quality (RCQ)

Quantifies how well **CMRA** normalizes the radiometric / modality gap — the mean absolute
deviation between the compensated thermal feature and the visible reference:

$$\mathrm{RCQ} = \frac{1}{N \cdot C}\,\bigl\|\mathbf{F}_{T}^{\mathrm{align}} - \mathbf{F}_{\rho}\bigr\|_1$$

where $N$ = valid spatial locations, $C$ = channels. **Lower is better.** Unlike end-task
accuracy, RCQ isolates the alignment mechanism itself (explicit physical parameterization
vs. implicit black-box fitting).

### Terrain Response Ratio (TRR)

Verifies that **TGM** is actively engaged rather than collapsing — the ratio of the
terrain-attributed feature norm to the aligned reference feature norm:

$$\mathrm{TRR} = \frac{\bigl\|\mathbf{F}_{\mathrm{ter}}\bigr\|_F}{\bigl\|\mathbf{F}_{\mathrm{ref}}\bigr\|_F + \epsilon}$$

**Higher** TRR ⇒ a larger share of the response is routed into the terrain branch (TGM
captures terrain-correlated responses); a near-zero TRR ⇒ the terrain branch has collapsed.

### Mean Total Variation (MTV)

Quantifies the TV smoothness penalty of **SAVR** — the mean $\ell_1$ gradient magnitude of
the refined map **outside** the ground-truth boundary band:

$$\mathrm{MTV} = \frac{1}{|\Omega \setminus \mathcal{B}_{\delta}|}\sum_{\mathbf{x}\in\Omega\setminus\mathcal{B}_{\delta}}\bigl(\|\nabla_h \mathbf{M}(\mathbf{x})\|_1 + \|\nabla_v \mathbf{M}(\mathbf{x})\|_1\bigr)$$

where $\Omega$ = evaluation domain, $\mathcal{B}_{\delta}$ = a $\delta$-pixel band around the
GT boundary. **Lower is better** (spurious non-boundary activations suppressed without
penalizing sharp true boundaries).

### Edge Alignment Score (EAS)

Quantifies the geometric refinement of **SAVR** — the F1 computed **only within a
$\delta{=}3$-pixel band** around the ground-truth change contour. Since boundaries are where
residual geometric noise produces soft activations, EAS directly reflects whether the
image-guided geometric regularizer aligns decision boundaries with the structural gradients
of the visible guidance image.

---

## 3. Cross-Modal Index

### Thermal Contribution Index (TCI)

Quantifies the net value of the thermal modality — the change-class F1 difference between
the RGB-TIR and RGB-only input settings:

$$\mathrm{TCI} = \mathrm{F1}_{\mathrm{chg}}(\text{RGB-TIR}) - \mathrm{F1}_{\mathrm{chg}}(\text{RGB})$$

Under the same architecture and training protocol, **positive** TCI ⇒ the thermal modality
brings a performance gain.

---

These metrics jointly evaluate detection accuracy and physics-grounded interpretability.
