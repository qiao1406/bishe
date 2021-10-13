import os
import re
from ..models import ModelRecord

# dir_path = 'C:\\WorkSpace\\bishe\\model\\model_paras'
dir_path = '../../../model/models/'

def init():
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        model_name, res, _ = re.split('[-.]+', file)
        observe_window, para_d, para_r, predict_gap, predict_len = [int(i) for i in re.findall(r'\d+', res)]

        mr = ModelRecord(model_name=model_name, observe_window=observe_window, predict_gap=predict_gap,
                         predict_len=predict_len, para_d=para_d, para_r=para_r, file_path=file_path)
        mr.save()
