from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory


def read_image(filepath):
    return ocr.ocr(filepath, cls=True)


def extract_data(filelist: list):
    _data = []
    for x in filelist:
        _data.append(read_image(x))
    return _data


if __name__ == '__main__':
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = './WechatIMG2.jpg'
    result = ocr.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

    print("fapiao")
    ocr = PaddleOCR(use_angle_cls=True, lang="ch",
                    page_num=2)  # need to run only once to download and load model into memory
    img_path = './fapiao1.pdf'
    result = ocr.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)