from math import dist
from statistics import mean
from numpy import mean, round_

def main():
    with open("input.txt", "r") as file:
        first_line = file.readline().split(" ")

        k = int(first_line[0])
        m = int(first_line[1])
        points = []
        for i in file:
            coords = tuple(float(j) for j in i.split())
            points.append(coords)

        centers = LloydsAlgorithm(points, k)
        for i in centers:
            print(i)

def LloydsAlgorithm(data, k):
    flag = True
    centers = []
    clusters = dict()
    for i in range(k):
        centers.append(data[i])
        clusters[i] = []

    while(flag):
        for i in range(len(data)):
            closest_center = None
            closest_center_dist = None
            for j in range(len(centers)):
                if (closest_center_dist is None or dist(data[i], centers[j]) < closest_center_dist):
                    closest_center = j
                    closest_center_dist = dist(data[i], centers[j])
            clusters[closest_center].append(data[i])

        flag = False
        for i in clusters:
            new_center = tuple(round_(mean(clusters[i], axis=0), decimals=3))
            if (new_center != centers[i]):
                flag = True
            centers[i] = new_center
            clusters[i] = []

    return centers

if __name__ == "__main__":
    main()