import requests

def generate_x_post(user_input: str) -> str:
    payload = {
        "model": "...",
        "input": "..."
    }
    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Authorization": f"Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
    )

def main():
    user_input = input("What should the post be about?")
    x_post = generate_x_post(user_input)
    print("Generated X Post:")
    print(x_post)

if __name__ == "__main__":
    main()
