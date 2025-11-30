## 🧠 YOLOv8 Yawn Detection – Model Summary

This project uses a custom-trained **YOLOv8 Detection Model** to classify and localize:

- **Yawn**
- **No Yawn**

The model is lightweight, fast, and suitable for real-time applications such as:
✅ Driver drowsiness detection  
✅ Student attention monitoring  
✅ Workplace fatigue analysis  

---

## ✅ Model Architecture

The model is based on **YOLOv8 DetectionModel**, consisting of:

- **Backbone:** CSPDarknet (Conv + C2f blocks)
- **Neck:** PAN/FPN for multi-scale feature fusion
- **Head:** YOLO detect layers (3 scales: P3, P4, P5)

---

## ✅ Model Summary (Key Stats)

| Metric | Value |
|--------|--------|
| **Model Type** | YOLOv8 (Custom) |
| **Total Parameters** | **3,011,238** |
| **Trainable Parameters** | **3,011,238** |
| **Non-Trainable Parameters** | **0** |
| **Model Size** | **12.04 MB** |
| **GFLOPs** | **8.2 GFLOPs** |
| **Runtime Memory** | ~240 MB |
| **Layers** | 129 |
| **Input Resolution** | 640 × 640 |
| **Output** | 8400 predictions × 6 values |

---

## ✅ Detection Performance

| Metric | Score |
|--------|--------|
| **Accuracy (Test Set)** | **99.84%** |
| **Correct Predictions** | 627 / 628 |
| **Only 1 Misclassification** | ✅ |
| **Speed** | ~5.6 ms per image |
| **Real-Time FPS (GPU)** | ~110 FPS |

---

## ✅ Model Memory Breakdown

| Category | Memory |
|----------|---------|
| **Input Size** | 4.92 MB |
| **Parameters** | 12.04 MB |
| **Forward/Backward Size** | 222.61 MB |
| **Total Estimated Runtime** | **239.57 MB** |

---

## ✅ Architecture Overview (Simplified)

YOLOv8
├── Backbone (CSPDarknet)
│ ├── Conv
│ ├── C2f Blocks
│ └── SPPF
├── Neck (PAN-FPN)
│ ├── Upsample
│ ├── Concat
│ └── C2f Blocks
└── Head (Detect)
├── P3 – Small objects
├── P4 – Medium objects
└── P5 – Large objects


---

## ✅ Example Use Cases

- Driver monitoring systems  
- Classroom monitoring  
- Health/fitness tracking  
- Smart CCTV fatigue detection  

---

## ✅ Model Export Options

The model can be exported to:

ONNX, TensorRT, OpenVINO, CoreML, TFLite


Example:

```python
model.export(format="onnx")



