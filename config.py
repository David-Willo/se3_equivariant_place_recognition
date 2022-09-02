####################
# GENERAL SETTINGS #
####################
''' DATA LOADER '''
# number of points for the input clouds
NUM_POINTS = 4096
# data path
DATASET_FOLDER = '/home/cel/data/benchmark_datasets'
# DATASET_FOLDER = '/home/cel/data/kitti'

#####################
# TRAINING SETTINGS #
#####################
''' GLOBAL '''
# specify the experient name, training process will be saved in the folder with the same name
EXP_NAME = 'e2pn_gem_exact_trainall' 
# choose the model to be trained from 'epn_netvlad' or 'atten_epn_netvlad'
MODEL = 'e2pn_gem' # 'e2pn_gem' # 'e2pn_netvlad'

''' TRAINING PICKLE FILES '''
# use the picke files in the following two lines for whole benchmark training
TRAIN_FILE = '/home/cel/data/benchmark_datasets/training_queries_baseline.pickle'
TEST_FILE = '/home/cel/data/benchmark_datasets/test_queries_baseline.pickle'
# use the picke files in the following two lines for a quick training with only 3 sequences in the benchmark
# TRAIN_FILE = '/home/cel/data/benchmark_datasets/training_queries_baseline_seq567.pickle'
# TEST_FILE = '/home/cel/data/benchmark_datasets/test_queries_baseline_seq567.pickle'

''' NETWORK DIMENSIONS '''
# output dimension of the global descriptor
GLOBAL_DESCRIPTOR_DIM = 256
# output dimension of the local feature
LOCAL_FEATURE_DIM = 1024
# number of points after attentive downsampling, not used if training with model 'epn_netvlad'
NUM_SELECTED_POINTS = 2048
# number of points if using stride in E2PN
# NUM_SUPERPOINTS = 512

''' DATA LOADER '''
# batch number setting, how many positive and negatives per query during training
BATCH_NUM_QUERIES = 1
TRAIN_POSITIVES_PER_QUERY = 2
TRAIN_NEGATIVES_PER_QUERY = 2
# Is this training resume from previous training?
RESUME = False

''' TRAINNING PARAMETERS '''
MAX_EPOCH = 30
BASE_LEARNING_RATE = 0.00005
MOMENTUM = 0.9
OPTIMIZER = 'adam'
DECAY_STEP = 200000
DECAY_RATE = 0.7

''' PARAMETERS FOR LOSS FUNCTION '''
LOSS_FUNCTION = 'quadruplet'
MARGIN_1 = 0.5
MARGIN_2 = 0.2
LOSS_LAZY = True
LOSS_IGNORE_ZERO_BATCH = False
TRIPLET_USE_BEST_POSITIVES = False

''' SAVE PATH '''
LOG_DIR = 'log/'
MODEL_FILENAME = "model.ckpt"

''' OTHERS '''
# setting GPU usage with CUDA_VISIBLE_DEVICES
GPU = '0'


#######################
# EVALUATION SETTINGS #
#######################
''' GLOBAL '''
# choose the model to evaluate from 'epn_netvlad' or 'atten_epn_netvlad'
EVAL_MODEL = 'e2pn_netvlad' # 'e2pn_gem' # 'e2pn_netvlad'
# the pretrained weights that you want to load into the model
RESUME_FILENAME = 'pretrained_model/e2pn_netvlad_v2_train3seq.ckpt'
# RESUME_FILENAME = 'pretrained_model/e2pn_netvlad_32_64_trainall.ckpt'
# RESUME_FILENAME = LOG_DIR+EXP_NAME+'/'+MODEL_FILENAME
# save paths for the evaluation results
# RESULTS_FOLDER = 'results/pr_evaluation_e2pn_netvlad_32_64_128_3seq'
RESULTS_FOLDER = 'results/pr_evaluation_e2pn_netvlad_v2_train3seq_eval'
OUTPUT_FILE = RESULTS_FOLDER+'/results.txt'

''' DATA LOADER '''
# batch number setting, how many positive and negatives per query during evaluation
EVAL_BATCH_SIZE = 1
EVAL_POSITIVES_PER_QUERY = 2
EVAL_NEGATIVES_PER_QUERY = 2

''' EVALUATION PICKLE FILES '''
# use the picke files in the following two lines for oxford benchmark evaluation
EVAL_DATABASE_FILE = '/home/cel/data/benchmark_datasets/oxford_evaluation_database.pickle'
EVAL_QUERY_FILE = '/home/cel/data/benchmark_datasets/oxford_evaluation_query.pickle'
# use the picke files in the following two lines for U.S. benchmark evaluation
# EVAL_DATABASE_FILE = '/home/cel/data/benchmark_datasets/university_evaluation_database.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/benchmark_datasets/university_evaluation_query.pickle'
# use the picke files in the following two lines for R.A. benchmark evaluation
# EVAL_DATABASE_FILE = '/home/cel/data/benchmark_datasets/residential_evaluation_database.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/benchmark_datasets/residential_evaluation_query.pickle'
# use the picke files in the following two lines for B.D. benchmark evaluation
# EVAL_DATABASE_FILE = '/home/cel/data/benchmark_datasets/business_evaluation_database.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/benchmark_datasets/business_evaluation_query.pickle'

# KITTI
# EVAL_DATABASE_FILE = '/home/cel/data/kitti/kitti_08_database_evaluate_new.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/kitti/kitti_08_queries_evaluate_new.pickle'
# EVAL_DATABASE_FILE = '/home/cel/data/kitti/kitti_08_database_evaluate_new.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/kitti/kitti_08_queries_evaluate_new.pickle'

# rotation only
# EVAL_DATABASE_FILE = '/home/cel/data/benchmark_datasets/oxford_evaluation_database_rot.pickle'
# EVAL_QUERY_FILE = '/home/cel/data/benchmark_datasets/oxford_evaluation_query_rot.pickle'

'''BASELINES TO PLOT (OPTIONAL)'''
POINTNETVLAD_RESULT_FOLDER = 'results/pr_evaluation_pointnetvlad'
SCANCONTEXT_RESULT_FOLDER = 'results/pr_evaluation_scan_context_oxford_evalall'
M2DP_RESULT_FOLDER = 'results/pr_evaluation_m2dp_evalall'
MINKLOC3D_RESULT_FOLDER = 'results/pr_evaluation_minkloc3d'
EPNNETVLAD_RESULT_FOLDER = 'results/pr_evaluation_atten_epn_netvlad_na60_trainall'
E2PNNETVLAD_RESULT_FOLDER = 'results/pr_evaluation_e2pn_netvlad_32_64_trainall'


'''cofig to string'''
def cfg_str():
    out_string = ""
    for name in globals():
        if not name.startswith("__") and not name.__contains__("cfg_str"):
            #print(name, "=", globals()[name])
            out_string = out_string + "cfg." + name + \
                "=" + str(globals()[name]) + "\n"
    return out_string
