from skimage.metrics import structural_similarity as ssim
import cv2

def compareImage(picPath_1, picPath_2):
    width = 1000
    height = 1000

    expected_image1 = cv2.imread(picPath_1)
    expected_image2 = cv2.imread(picPath_2)
    # ssim方法需要两个图片尺寸相同
    expected_image_resized1 = cv2.resize(expected_image1, (width, height))
    expected_image_resized2 = cv2.resize(expected_image2, (width, height))
    # 转换为灰度图片
    pic1_gray = cv2.cvtColor(expected_image_resized1, cv2.COLOR_RGB2GRAY)
    pic2_gray = cv2.cvtColor(expected_image_resized2, cv2.COLOR_RGB2GRAY)
    # 计算结构相似性指数
    ssim_index = ssim(pic1_gray, pic2_gray)
    print("the similar value is：" + str(ssim_index))
    return ssim_index