def auto_a_b (file_name):
    
    import numpy as np
    import cv2
    
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    cum_hist = hist.cumsum()

    tr = round( 0.02 * cum_hist.max() )
    a_y = cum_hist.min() + tr
    b_y = cum_hist.max() - tr

    a_candidate = []
    b_candidate = []

    for item in cum_hist:
        res_a = abs(item - a_y)
        res_b = abs(item - b_y) 
        a_candidate.append(res_a)
        b_candidate.append(res_b)

    min_a = min(a_candidate)    
    min_b = min(b_candidate)

    final_a = a_candidate.index(min_a)
    final_b = b_candidate.index(min_b)  

    x = np.array([final_a, final_b])
    y = np.array([0, 0])

    return x, y  

#check
# from matplotlib import pyplot as plt
# import cv2
# file_name = 'train.jpg'
# img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

# x, y =auto_a_b(file_name)

# plt.title(label = file_name)
# plt.scatter(x , y, color = 'hotpink', s = 200 )
# plt.hist(img.ravel(), 256, [0,256], alpha = 0.5)
# save_name = file_name[:-4] + 'plot'
# plt.savefig(save_name)
# plt.show()

