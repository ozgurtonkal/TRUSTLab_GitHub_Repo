[README.md](https://github.com/user-attachments/files/31388780/README.md)
# TRUSTLab Cross-Dataset Generalization — Supplementary Materials

This repository contains the analysis scripts, raw experimental results, and
manuscript source for:

> Tonkal, Ö. (2026). Cross-Dataset Generalization of the TRUSTLab Dataset in
> Network Intrusion Detection: A Comparative Machine and Deep Learning Study.
> \*Journal of Information Security and Applications\* (submitted).

## Repository Structure

```
manuscript/
    paper.tex          - Full LaTeX source (Elsevier CAS-SC template)
    cas-refs.bib        - Bibliography (26 references)

figures/
    scripts/            - Python (matplotlib) scripts that generate all 8 figures
    output/              - Pre-rendered 300 DPI PNG outputs of the 8 figures

data/
    raw\_results/         - Raw CSV outputs from the Kaggle training/evaluation
                            runs (multi-seed, bootstrap, ablation, drift metrics)
    processed\_tables/    - The 14 tables reported in the paper (Tables 1-10,
                            including sub-tables 4a-4d), extracted as CSV
```

models/
Used all .pkl and keras models

## Datasets Used (Not Redistributed Here)

This study uses three publicly available datasets, cited in full in the
manuscript. They are **not** redistributed in this repository; please obtain
them from their original sources:

* **TRUSTLab** (2026) — Villafranca, Tasic \& Cano, *Frontiers in Computer
Science*. https://doi.org/10.3389/fcomp.2026.1803271
* **CICIDS2017** — Sharafaldin, Habibi Lashkari \& Ghorbani (2018), ICISSP.
Available via the Canadian Institute for Cybersecurity (CIC) dataset page.
* **CSE-CIC-IDS2018** — Available via the CIC dataset page (AWS-hosted
version) / registry.opendata.aws.

## Raw Results File Guide

|File|Corresponds to|
|-|-|
|`seed\_{42,123,2024}\_results.csv`|Multi-seed binary classification (Table 10)|
|`seed\_{42,123,2024}\_full\_metrics.csv`|Same runs with full Accuracy/Precision/Recall (Tables 5, 7, 10)|
|`Top5\_seed\*\_results.csv`, `Top10\_seed\*\_results.csv`|Feature-count ablation (Section 4.6, Figure 8)|
|`ALL\_ablation\_multiseed\_results.csv`|Combined ablation results across all seeds|
|`drift\_severity\_4metric.csv`|KS/KL/JS/Wasserstein 4-metric drift verification (Table 4a)|
|`NIHAI\_cross\_dataset\_binary\_results.csv`|Cross-dataset MCC source run (Table 8)|
|`NIHAI\_indomain\_\*`|Within-dataset reference run (binary \& multiclass)|
|`bootstrap\_CI\_DDoS\_DoS\_PortScan.csv`|Bootstrap 95% CI, large-sample families (Figure 7, Table 9 support)|

## Reproducing the Manuscript PDF

```bash
cd manuscript
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

Note: `paper.tex` expects the Elsevier `cas-sc.cls` / `cas-common.sty`
template files and a `figures/` subfolder containing the 8 PNGs from
`figures/output/` in this repository — copy or symlink accordingly, or
adjust the `\\includegraphics` paths.

## Reproducing the Figures

Each script in `figures/scripts/` is self-contained and writes a single
300 DPI PNG to its output path (edit the `savefig(...)` path at the bottom
of each script as needed). Requires `matplotlib`.

## License

Code and figure-generation scripts in this repository are released under
the MIT License. The manuscript text is © the author; please cite the
published paper if reusing findings or figures.

## Contact

Özgür Tonkal — ozgur.tonkal@samsun.edu.tr
Department of Software Engineering, Faculty of Computer and Information
Sciences, Samsun University, Türkiye.
ORCID: 0000-0001-7219-9053

