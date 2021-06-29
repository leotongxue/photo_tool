import glob
import xml.etree.ElementTree as ET
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from kmeans import kmeans, avg_iou

ANNOTATIONS_PATH = "/Users/leo/Desktop/yolov5-new/data/Annotations"
#以正斜杠/这种形式可以防止反斜杠带来的转义错误
CLUSTERS = 9
BBOX_NORMALIZE = True

def show_cluster(data, cluster, max_points=2000):
    if len(data) > max_points:
        idx = np.random.choice(len(data),max_points)
        data = data[idx]
    plt.scatter(data[:, 0], data[:, 1], s=5, c='lavender')
    plt.scatter(cluster[:, 0], cluster[:, 1], c='red', s=100, marker="^")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.title("Bounding and anchor distribution")
    plt.savefig("cluster.png")
    plt.show()

def show_w_h(data,cluster,bins=50):
    if data.dtype != np.float32:
        data = data.astype(np.float32)
    width = data[:, 0]
    height = data[:, 1]
    ratio = height / width

    plt.figure(1, figsize=(20, 6))
    plt.subplot(131)
    plt.hist(width, bins=bins, color='blue', rwidth=0.8)
    plt.xlabel('Width')
    plt.ylabel('Number')
    plt.grid(True, linestyle='-.')
    plt.title('Distribution of Width')

    plt.subplot(132)
    plt.hist(height, bins=bins, color='green', rwidth=0.8)
    plt.xlabel('Height')
    plt.ylabel('Number')
    plt.grid(True, linestyle='-.')
    plt.title('Distribution of Height')

    plt.subplot(133)
    plt.hist(ratio, bins=bins, color='magenta', rwidth=0.8)
    plt.xlabel('Height / Width')
    plt.ylabel('Number')
    plt.grid(True, linestyle='-.')
    plt.title('Distribution of aspect ratio[Height / Width]')
    plt.savefig("shape-distribution.png")
    plt.show()

def sort_cluster(cluster):
    if cluster.dtype != np.float32:
        cluster = cluster.astype(np.float32)
    area = cluster[:, 0] * cluster[:, 1]
    ratio = cluster[:, 1:2] / cluster[:, 0:1]
    return np.concatenate([cluster, ratio], axis=-1)

def load_dataset(path):
    dataset = []
    for xml_file in tqdm.tqdm(glob.glob("{}/*xml".format(path))):
        print(xml_file)
        tree = ET.parse(xml_file)

        height = int(tree.findtext("./size/height"))
        width = int(tree.findtext("./size/width"))

        for obj in tree.iter("object"):
            xmin = int(float(obj.findtext("bndbox/xmin"))) / width
            ymin = int(float(obj.findtext("bndbox/ymin"))) / height
            xmax = int(float(obj.findtext("bndbox/xmax"))) / width
            ymax = int(float(obj.findtext("bndbox/ymax"))) / height

            dataset.append([xmax - xmin, ymax - ymin])

    return np.array(dataset)


data = load_dataset(ANNOTATIONS_PATH)
print(ANNOTATIONS_PATH)
out = kmeans(data, k=CLUSTERS)
out_sorted = sort_cluster(out)
if out.dtype != np.float32:
    cluster = out.astype(np.float32)
show_cluster(data, out, max_points=2000)

show_w_h(data, out, bins=50)
