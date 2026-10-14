# Canvas

A physically interpretable optical–thermal change detection framework for landslide assessment.

---

## Datasets

### 1. VT-CD

A visible–thermal bi-temporal change-detection dataset for landslide scenes.
Each sample is a registered pre-/post-event pair.

- Modalities: Visible (RGB) + Thermal (TIR)

### 2. EQ-Ext

Earthquake extension sets for cross-regional / cross-disaster generalization
(4-channel, RGB + TIR).

### Directory Layout

```
<dataset>/
├── A/          # pre-event optical (RGB)
├── B/          # post-event optical (RGB)
├── A_TIR/      # pre-event thermal (TIR)
├── B_TIR/      # post-event thermal (TIR)
└── label/      # binary change mask
```

> **Only a few sample pairs are released** (see `sample_data/`) to illustrate the format.
> The **full dataset** and the **train/val/test split files** are **NOT included**.
> **To obtain the full dataset for running experiments, please contact the authors.**

---

## Sample Data

`sample_data/` contains a handful of sample pairs only:

```
sample_data/
├── VT-CD/
├── EQ-Ext/
│   ├── Jishishan/
│   └── Jiashi/
```

---

## Code

| Path | Content |
| --- | --- |
| `canvas/` | method modules: `CMRA`, `TGM`, `SAVR`, `Canvas` |
| `metrics.py` | evaluation toolkit (standard + physics + cross-modal metrics) |
| `gen_public_arch.py` | generates the public architecture diagram |

> Only the **key structural part** of the method is released.

---

## Citation

If you use this work, please cite the Canvas paper.

## License

Released for **non-commercial academic research** only. See `LICENSE`.
