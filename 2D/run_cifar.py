from typing import Dict
from data_pipeline import load_cifar

def run_cifar(inputs: Dict[str, str]):
    """Classify CIFAR-100 dataset

    Args:
        inputs (Dict): must contain:
            - meta_path: path where meta file is stored
            - train_path: path wherte train pickled data is stored
            - test_path: path where test pickled data is stored
    """
    loaded_data = load_cifar(
        inputs['meta_path'], 
        inputs['train_path'],
        inputs['test_path']
    )
    import pdb;pdb.set_trace()

def main():
    input_d = {
        'meta_path':'../../data/CIFAR-100/meta',
        'train_path':'../../data/CIFAR-100/train',
        'test_path':'../../data/CIFAR-100/test'
    }
    run_cifar(input_d)
    
if __name__ == '__main__':
    main()