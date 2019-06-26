import torch
def categorical_accuracy(preds, y):
    """
    Returns accuracy per batch
    """
    max_preds = preds.argmax(dim = 1, keepdim = True) # get the index of the max probability 여기서 argmax를 찾는다
    correct = max_preds.squeeze(1).eq(y) # 같은것만 찾는 코드
    return correct.sum() / torch.FloatTensor([y.shape[0]])
