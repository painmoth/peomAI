from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 默认的Ollama API地址
OLLAMA_API_URL = "http://localhost:11434/api/generate"



@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/set_api', methods=['POST'])
def set_api():
    global OLLAMA_API_URL
    data = request.json
    OLLAMA_API_URL = data.get('api_url')
    return jsonify({"status": "success", "message": f"API URL updated to {OLLAMA_API_URL}"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    model_name = data.get('model', 'qwen2.5:7b')  # 添加模型参数，默认为llama2
    
    # 准备发送给Ollama的请求
    ollama_data = {
        "model": model_name,  # 使用从请求中获取的模型名称
        "prompt": user_message,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=ollama_data)
        if response.status_code == 200:
            bot_response = response.json().get('response', '')
            return jsonify({"response": bot_response})
        else:
            return jsonify({"error": "Failed to get response from Ollama"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/save_conversations', methods=['POST'])
def save_conversations():
    data = request.json
    conversations = data.get('conversations', [])
    filename = data.get('filename', 'script_draft.txt')
    
    try:
        # 添加调试信息
        print("Received conversations data:", conversations)
        print("Type of conversations:", type(conversations))
        
        with open(filename, 'w', encoding='utf-8') as f:
            for conv in conversations:
                # 直接写入消息序号和内容
                f.write(f"Message {conversations.index(conv) + 1}:\n")
                f.write(f"{conv}\n\n")
        
        return jsonify({
            "status": "success", 
            "message": f"Conversations saved to {filename}"
        })
    except Exception as e:
        print(f"Error saving conversations: {str(e)}")
        print(f"Conversations data: {conversations}")  # 打印完整的会话数据
        return jsonify({
            "error": f"Failed to save conversations: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
