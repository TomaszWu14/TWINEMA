# Przekazanie — stan projektu i następny krok (F5)

> 13 nodes · cohesion 0.23

## Key Concepts

- **segmentation.py** (10 connections) — `web/ml/segmentation.py`
- **segment()** (8 connections) — `web/ml/segmentation.py`
- **kmeans()** (4 connections) — `web/ml/segmentation.py`
- **features()** (3 connections) — `web/ml/segmentation.py`
- **_name()** (3 connections) — `web/ml/segmentation.py`
- **_demo()** (2 connections) — `web/ml/segmentation.py`
- **_dist2()** (2 connections) — `web/ml/segmentation.py`
- **_standardize()** (2 connections) — `web/ml/segmentation.py`
- **ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…** (1 connections) — `web/ml/segmentation.py`
- **{materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem.** (1 connections) — `web/ml/segmentation.py`
- **k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego…** (1 connections) — `web/ml/segmentation.py`
- **Nazwa i rekomendacja z pozycji centroidu wśród segmentów (rotacja, regularność).** (1 connections) — `web/ml/segmentation.py`
- **→ wynik do zapisu w ModelRun: segmenty z profilem, liczebnością, udziałem…** (1 connections) — `web/ml/segmentation.py`

## Relationships

- [blender_stock.py](blender_stock.py.md) (2 shared connections)
- [roles.py](roles.py.md) (1 shared connections)

## Source Files

- `web/ml/segmentation.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*