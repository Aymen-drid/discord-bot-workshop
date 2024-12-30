import aiohttp
import asyncio

async def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    
    try:
        session = aiohttp.ClientSession()
        response = await session.get(url)
        
        if response.status == 200:
            data = await response.json()
            print(f"\nName: {data['name']}")
            print(f"Height: {data['height']}")
            print(f"Weight: {data['weight']}")
        else:
            print("Pokemon not found!")
            
        await session.close()
        
    except Exception as e:
        print(f"Error: {e}")

# Run the program
pokemon = "pikachu"
asyncio.run(get_pokemon(pokemon))