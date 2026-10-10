import cv2
import numpy as np
import matplotlib.pyplot as plt


# 1. HISTOGRAM CALCULATION

def histogram_calculation(img):
    histogram = np.zeros(256, dtype=int)

    for pixel in img.flatten():
        histogram[pixel] += 1

    return histogram

# 2. HISTOGRAM EQUALIZATION

def histogram_equalization(img):
    hist = histogram_calculation(img)

    total_pixel = img.size

    # PDF
    pdf = hist / total_pixel

    # CDF
    cdf = np.cumsum(pdf)

    # Mapping pixel baru
    mapping = np.round(cdf * 255)
    mapping = np.clip(mapping, 0, 255).astype(np.uint8)

    result = mapping[img]

    return result

# 3. HISTOGRAM SPECIFICATION 

def histogram_specification(img, reference):

    # Histogram input dan reference
    hist_input = histogram_calculation(img)
    hist_ref = histogram_calculation(reference)

    # PDF
    pdf_input = hist_input / img.size
    pdf_ref = hist_ref / reference.size

    # CDF
    cdf_input = np.cumsum(pdf_input)
    cdf_ref = np.cumsum(pdf_ref)

    # Mapping
    mapping = np.zeros(256, dtype=np.uint8)

    for i in range(256):
        difference = np.abs(cdf_ref - cdf_input[i])

        mapping[i] = np.argmin(difference)

    result = mapping[img]

    result = np.round(result)
    result = np.clip(result, 0, 255)

    return result.astype(np.uint8)

# TAMPILKAN HISTOGRAM

def show_histogram(img, title):
    hist = histogram_calculation(img)

    plt.plot(hist)
    plt.title(title)
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 255])

def main():

    # Baca grayscale
    input_img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
    reference_img = cv2.imread("reference.png", cv2.IMREAD_GRAYSCALE)

    if input_img is None:
        print("input.jpg tidak ditemukan!")
        return

    if reference_img is None:
        print("reference.jpg tidak ditemukan!")
        return

    # Optional supaya tampilan tidak terlalu besar
    input_img = cv2.resize(input_img, (300, 300))
    reference_img = cv2.resize(reference_img, (300, 300))

    # TEST HISTOGRAM CALCULATION

    histogram_input = histogram_calculation(input_img)

    print("Histogram berhasil dihitung")
    print("Jumlah pixel:", np.sum(histogram_input))

    # TEST HISTOGRAM EQUALIZATION

    equalized_img = histogram_equalization(input_img)

    # TEST HISTOGRAM SPECIFICATION

    specified_img = histogram_specification(
        input_img,
        reference_img
    )

    # TAMPIL GAMBAR

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(input_img, cmap="gray")
    plt.title("Input Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(equalized_img, cmap="gray")
    plt.title("Histogram Equalization")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(reference_img, cmap="gray")
    plt.title("Reference Image")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(specified_img, cmap="gray")
    plt.title("Histogram Specification")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # TAMPIL HISTOGRAM

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    show_histogram(
        input_img,
        "Histogram Input"
    )

    plt.subplot(2, 2, 2)
    show_histogram(
        equalized_img,
        "Histogram Equalized"
    )

    plt.subplot(2, 2, 3)
    show_histogram(
        reference_img,
        "Histogram Reference"
    )

    plt.subplot(2, 2, 4)
    show_histogram(
        specified_img,
        "Histogram Specification"
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()