import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.reshape(list, (3,3))

    output = {
        'mean': [np.mean(matrix, axis=0).tolist(),np.mean(matrix, axis=1).tolist(),np.mean(list)],
        'variance': [np.var(matrix, axis=0).tolist(),np.var(matrix, axis=1).tolist(),np.var(list)],
        'standard deviation': [np.std(matrix, axis=0).tolist(),np.std(matrix, axis=1).tolist(),np.std(list)],
        'max': [np.max(matrix, axis=0).tolist(),np.max(matrix, axis=1).tolist(),np.max(list)],
        'min': [np.min(matrix, axis=0).tolist(),np.min(matrix, axis=1).tolist(),np.min(list)],
        'sum': [np.sum(matrix, axis=0).tolist(),np.sum(matrix, axis=1).tolist(),np.sum(list)]
    }

    print(output)
    return output


calculate([2,6,2,8,4,0,1,5,7])