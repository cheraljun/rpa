from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# 加载抗日战争数据源
def load_kangri_data():
    data_file = "kangri_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 以 ### 分割内容
        segments = content.split("###")
        # 去除空白段并返回
        return [segment.strip() for segment in segments if segment.strip()]

# 加载博弈论数据源
def load_gametheory_data():
    data_file = "game-theroy_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]

# 加载王阳明语录数据源
def load_wymtalk_data():
    data_file = "being-a-sage_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]

# 加载乔治奥威尔语录数据源
def load_orwelltalk_data():
    data_file = "orwell_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]

# 加载黑格尔语录数据源
def load_hegaltalk_data():
    data_file = "hegal_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]
    
# 加载英语单词数据源
def load_vocabulary_data():
    data_file = "vocabulary_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]
    
# 加载鲁迅语录数据源
def load_luxuntalk_data():
    data_file = "luxun_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白段并返回
        return [segment.strip() for segment in segments if segment.strip()]
    
# 加载猫咪家庭医学大百科数据源
def load_catcare_data():
    data_file = "catcare_text.txt"
    # 检查文件是否存在，若不存在则返回空列表
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r", encoding="utf-8") as f:
        content = f.read()
        # 按行分割内容
        segments = content.splitlines()
        # 去除空白行并返回
        return [segment.strip() for segment in segments if segment.strip()]
    


# 初始化数据
KANGRI_DATA = load_kangri_data()
GAMETHEORY_DATA = load_gametheory_data()
WYMTALK_DATA = load_wymtalk_data()
HEGALTALK_DATA = load_hegaltalk_data()
VOCABULARY_DATA = load_vocabulary_data()
LUXUNTALK_DATA = load_luxuntalk_data()
ORWELLTALK_DATA = load_orwelltalk_data()
CATCARE_DATA = load_catcare_data()

# 抗日战争 API 路由
@app.route("/kangri", methods=["GET"])
def get_kangri():
    # 若数据源为空，返回错误信息
    if not KANGRI_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 若数据源记录不足5条，返回错误信息
    if len(KANGRI_DATA) < 5:
        return jsonify({
            "status": "error",
            "message": "数据源记录不足5条，无法按要求输出"
        }), 404
    # 随机选择一个起始索引，确保后续还有5条记录
    random_index = random.randint(0, len(KANGRI_DATA) - 5)
    # 选取连续的5条记录
    kangri = "\n".join(KANGRI_DATA[random_index:random_index + 5])
    return jsonify({
        "status": "success",
        "data": kangri
    }), 200

# 抗日战争 API 路由
# @app.route("/kangri", methods=["GET"])
# def get_kangri():
#     if not KANGRI_DATA:
#         return jsonify({
#             "status": "error",
#             "message": "数据源为空或文件不存在"
#         }), 404
#     kangri = random.choice(KANGRI_DATA)
#     return jsonify({
#         "status": "success",
#         "data": kangri
#     }), 200

# 博弈论 API 路由
@app.route("/gametheory", methods=["GET"])
def get_gametheory():
    # 若数据源为空，返回错误信息
    if not GAMETHEORY_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 若数据源记录不足2条，返回错误信息
    if len(GAMETHEORY_DATA) < 2:
        return jsonify({
            "status": "error",
            "message": "数据源记录不足2条，无法按要求输出"
        }), 404
    # 随机选择一个起始索引，确保后续还有2条记录
    random_index = random.randint(0, len(GAMETHEORY_DATA) - 2)
    # 选取连续的5条记录
    gametheory = "\n".join(GAMETHEORY_DATA[random_index:random_index + 2])
    return jsonify({
        "status": "success",
        "data": gametheory
    }), 200

# 博弈论 API 路由
# @app.route("/gametheory", methods=["GET"])
# def get_gametheory():
#     # 若数据源为空，返回错误信息
#     if not GAMETHEORY_DATA:
#         return jsonify({
#             "status": "error",
#             "message": "数据源为空或文件不存在"
#         }), 404
#     # 随机选择一条记录
#     gametheory = random.choice(GAMETHEORY_DATA)
#     return jsonify({
#         "status": "success",
#         "data": gametheory
#     }), 200

# 王阳明语录 API 路由
@app.route("/wymtalk", methods=["GET"])
def get_sage():
    # 若数据源为空，返回错误信息
    if not WYMTALK_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 若数据源记录不足3条，返回错误信息
    if len(WYMTALK_DATA) < 3:
        return jsonify({
            "status": "error",
            "message": "数据源记录不足3条，无法按要求输出"
        }), 404
    # 随机选择一个起始索引，确保后续还有3条记录
    random_index = random.randint(0, len(WYMTALK_DATA) - 3)
    # 选取连续的3条记录
    wymtalk = "\n".join(WYMTALK_DATA[random_index:random_index + 3])
    return jsonify({
        "status": "success",
        "data": wymtalk
    }), 200

# 黑格尔语录 API 路由
@app.route("/hegaltalk", methods=["GET"])
def get_phd():
    # 若数据源为空，返回错误信息
    if not HEGALTALK_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 随机选择一条记录
    hegaltalk = random.choice(HEGALTALK_DATA)
    return jsonify({
        "status": "success",
        "data": hegaltalk
    }), 200

# 乔治奥威尔语录 API 路由
@app.route("/orwelltalk", methods=["GET"])
def get_orwelltalk():
    # 若数据源为空，返回错误信息
    if not ORWELLTALK_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 随机选择一条记录
    orwelltalk = random.choice(ORWELLTALK_DATA)
    return jsonify({
        "status": "success",
        "data": orwelltalk
    }), 200

# 英语单词 API 路由
@app.route("/vocabulary", methods=["GET"])
def get_vocabulary():
    # 若数据源为空，返回错误信息
    if not VOCABULARY_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 随机选择一条记录
    vocabulary = random.choice(VOCABULARY_DATA)
    return jsonify({
        "status": "success",
        "data": vocabulary
    }), 200

'''# 英语单词 API 路由
@app.route("/vocabulary", methods=["GET"])
def get_vocabulary():
    # 若数据源为空，返回错误信息
    if not VOCABULARY_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 若数据源记录不足2条，返回错误信息
    if len(VOCABULARY_DATA) < 2:
        return jsonify({
            "status": "error",
            "message": "数据源记录不足2条，无法按要求输出"
        }), 404
    # 随机选择一个起始索引，确保后续还有5条记录
    random_index = random.randint(0, len(VOCABULARY_DATA) - 2)
    # 选取连续的5条记录
    vocabulary = "\n".join(VOCABULARY_DATA[random_index:random_index + 2])
    return jsonify({
        "status": "success",
        "data": vocabulary
    }), 200'''

# 鲁迅语录 API 路由
@app.route("/luxuntalk", methods=["GET"])
def get_luxuntalk():
    # 若数据源为空，返回错误信息
    if not LUXUNTALK_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 随机选择一条记录
    luxuntalk = random.choice(LUXUNTALK_DATA)
    return jsonify({
        "status": "success",
        "data": luxuntalk
    }), 200

# 猫咪家庭医学大百科 API 路由
@app.route("/catcare", methods=["GET"])
def get_catcare():
    # 若数据源为空，返回错误信息
    if not CATCARE_DATA:
        return jsonify({
            "status": "error",
            "message": "数据源为空或文件不存在"
        }), 404
    # 若数据源记录不足2条，返回错误信息
    if len(CATCARE_DATA) < 2:
        return jsonify({
            "status": "error",
            "message": "数据源记录不足2条，无法按要求输出"
        }), 404
    # 随机选择一个起始索引，确保后续还有2条记录
    random_index = random.randint(0, len(CATCARE_DATA) - 2)
    # 选取连续的5条记录
    catcare = "\n".join(CATCARE_DATA[random_index:random_index + 2])
    return jsonify({
        "status": "success",
        "data": catcare
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=49152, debug=True)    