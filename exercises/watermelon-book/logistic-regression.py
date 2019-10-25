# encoding: utf-8
"""
@author:max bay 
@version: python 3.6
@time: 2018/6/2 20:55
"""
 
import numpy as np
 
# Logistic 回归梯度上升优化算法
def load_data_set():
    # 创建两个列表
    data_mat = []
    label_mat = []
    fr = open('data3.0-alpha.csv')
    fr.readline()
    for line in fr.readlines():
        # 对当前行去除首尾空格，并按空格进行分离
        line_arr = line.strip().split(',')
        #data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
        data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
        label_mat.append(int(line_arr[2]))
    return data_mat[1:], label_mat[1:]
 
 
def sigmoid(inx):
 
    return 1.0 / (1 + np.exp(-inx))
    # return 0.5 * (1 + np.tanh(0.5 * inx))
 
 
def grad_ascent(data_mat_in, class_labels):
    data_matrix = np.mat(data_mat_in)  # convert to NumPy matrix
    label_mat = np.mat(class_labels).transpose()  # convert to NumPy matrix
    m, n = np.shape(data_matrix)
    alpha = 0.001
    max_cycles = 500
    weights = np.ones((n, 1))
    for k in range(max_cycles):  # heavy on matrix operations
        h = sigmoid(data_matrix * weights)  # matrix mult
        error = (label_mat - h)  # vector subtraction
        weights = weights + alpha * data_matrix.transpose() * error  # matrix mult
    return weights
 
 
# 画出数据集和Logistic回归最佳拟合直线的函数
def plot_best_fit(weights):
    import matplotlib.pyplot as plt
    data_mat, label_mat = load_data_set()
    data_arr = np.array(data_mat)
    n = np.shape(data_arr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(label_mat[i]) == 1:
            xcord1.append(data_arr[i, 1])
            ycord1.append(data_arr[i, 2])
        else:
            xcord2.append(data_arr[i, 1])
            ycord2.append(data_arr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
 
 
def stoc_grad_ascent0(data_matrix, class_labels):
    m, n = np.shape(data_matrix)
    alpha = 0.01
    weights = np.ones(n)  # initialize to all ones
    for i in range(m):
        h = sigmoid(sum(data_matrix[i] * weights))
        error = class_labels[i] - h
        weights = weights + alpha * error * data_matrix[i]
    return weights
 
 
# 改进的随机梯度上升算法
def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):
    m, n = np.shape(data_matrix)
    weights = np.ones(n)  # initialize to all ones
    for j in range(num_iter):
        data_index = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.0001  # apha decreases with iteration, does not
            rand_index = int(np.random.uniform(0, len(data_index)))  # go to 0 because of the constant
            h = sigmoid(sum(data_matrix[rand_index] * weights))
            error = class_labels[rand_index] - h
            weights = weights + alpha * error * data_matrix[rand_index]
            del (data_index[rand_index])
    return weights
 
 
# Logistic回归分类函数
def classify_vector(inx, weights):
    """
    它以回归系数和特征向量作为输入来计算对应的Sigmoid值。
    如果Sigmoid值大于0.5函数返回1，否则返回0。
    """
    prob = sigmoid(sum(inx * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0
 
 
def colic_test():
    fr_train = open('horseColicTraining.txt')
    fr_test = open('horseColicTest.txt')
    training_set = []
    training_labels = []
    for line in fr_train.readlines():
        curr_line = line.strip().split('\t')
        line_arr = []
        for i in range(21):
            line_arr.append(float(curr_line[i]))
        training_set.append(line_arr)
        training_labels.append(float(curr_line[21]))
    train_weights = stoc_grad_ascent1(np.array(training_set), training_labels, 1000)
    error_count = 0
    num_test_vec = 0.0
    for line in fr_test.readlines():
        num_test_vec += 1.0
        curr_line = line.strip().split('\t')
        line_arr = []
        for i in range(21):
            line_arr.append(float(curr_line[i]))
        if int(classify_vector(np.array(line_arr), train_weights)) != int(curr_line[21]):
            error_count += 1
    error_rate = (float(error_count) / num_test_vec)
    print("the error rate of this test is: %f" % error_rate)
    return error_rate
 
 
def multi_test():
    num_tests = 10
    error_sum = 0.0
    for k in range(num_tests):
        error_sum += colic_test()
    print("after %d iterations the average error rate is: %f" % (num_tests, error_sum / float(num_tests)))
 
 
if __name__ == '__main__':
    dataMat, labelMat = load_data_set()
    # weights = grad_ascent(dataMat, labelMat)
    weights = stoc_grad_ascent1(np.array(dataMat), labelMat)
    plot_best_fit(weights)
    # multi_test()
