import pickle
from typing import Dict

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def load_cifar(meta: str, train: str, test: str) -> Dict[str, Dict]:
    """Load cifar raw pickled files into memorary

    Args:
        meta (str): meta data pickled file path
        train (str): train data pickled file path
        test (str): test data pickled file path

    Returns:
        Dict[str, Dict]: Contains memory loaded CIFAR-100 data
    """
    meta_data_d = unpickle(meta)
    train_data_d = unpickle(train)
    test_data_d = unpickle(test)
    
    loaded_data = {
        'superclass_dict': dict(list(enumerate(
            meta_data_d[b'coarse_label_names']))),
        'train_data': train_data_d[b'data'],
        'train_labels': train_data_d[b'coarse_labels'],
        'test_data': test_data_d[b'data'],
        'test_labels': test_data_d[b'coarse_labels']
    }
    
    return loaded_data