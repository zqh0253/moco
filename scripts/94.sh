python main_moco.py 
-a resnet34 \  
--lr 0.03 \
--batch-size 256 --moco-k 40960\
--dist-url 'tcp://localhost:10001' --multiprocessing-distributed --world-size 1 --rank 0 /home/yhxu/qhzhang/workspace/ytb

