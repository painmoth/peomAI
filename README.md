# peomAI
用chat的方式写诗

要运行这个程序，你需要：
1. 安装必要的依赖：
pip install flask requests

2. 确保Ollama服务已经在运行

3. 运行Python脚本：
python chat.py

4. 在浏览器中访问 http://localhost:5001
   
这个实现包含以下功能：
* 简洁的聊天界面
* 可以设置Ollama API的地址
* 支持发送消息和接收回复
* 消息历史显示
* 支持回车键发送消息
* 支持选中消息并保存到对应的文件中
* 错误处理
* 响应式设计

你可以根据需要修改样式或添加更多功能。默认使用的是llama2模型，你可以在Python代码中修改model参数来使用其他Ollama支持的模型。
