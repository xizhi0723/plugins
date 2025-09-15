# 导入必要的库
import comfy           # ComfyUI核心库
import nodes           # ComfyUI节点基类
import folder_paths    # ComfyUI文件路径工具
import librosa         # 音频处理库（用于获取时长）

# 定义节点类，继承自ComfyUI的Node基类
class AudioDurationNode(nodes.Node):
    # 定义节点的输入参数
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {  # 必选参数
                # 输入音频文件路径，类型为字符串，默认空
                "audio_file": ("STRING", {"default": "", "dynamicPrompts": False})
            }
        }
    
    # 定义节点的输出类型和名称
    RETURN_TYPES = ("FLOAT",)  # 输出类型：浮点数（时长，单位秒）
    RETURN_NAMES = ("duration_sec",)  # 输出端口显示名称："duration_sec"
    FUNCTION = "execute"  # 节点运行时调用的函数名
    CATEGORY = "Audio Processing"  # 节点在ComfyUI中的分类（显示在哪个菜单下）

    # 核心执行函数：计算音频时长
    def execute(self, audio_file: str) -> tuple:
        # 获取音频文件的完整路径（处理ComfyUI的文件引用格式）
        full_path = folder_paths.get_annotated_filepath(audio_file.strip())
        # 用librosa库读取音频文件并获取时长
        duration = librosa.get_duration(filename=full_path)
        # 返回时长（转为浮点数）
        return (float(duration),)

# 注册节点到ComfyUI（固定格式）
NODE_CLASS_MAPPINGS = {"AudioDurationNode": AudioDurationNode}
# 节点在UI中显示的名称
NODE_DISPLAY_NAME_MAPPINGS = {"AudioDurationNode": "📏 Audio Duration (开源版)"}
    
