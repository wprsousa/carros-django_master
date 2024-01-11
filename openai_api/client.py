from openai import OpenAI

client = OpenAI()


def get_car_ai_bio(model, brand, year):
    prompt = """
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas 
    específicas desse modelo.
    """
    prompt = prompt.format(brand, model, year)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1000
    )
    return response.choices[0].text
