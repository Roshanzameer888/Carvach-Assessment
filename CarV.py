from fastapi import FastAPI, Body, Path

app = FastAPI()

class User:
    id: int
    username: str
    email: str
    password: str

@app.post("/users", response_model=User)
async def create_user(user: User = Body(...)):
    # Create a new user in the database
    # ...

    # Return the created user
    return user

@app.get("/users", response_model=List[User])
async def get_all_users():
    # Get all users from the database
    # ...

    # Return the list of users
    return users

@app.get("/users/{id}", response_model=User)
async def get_user_by_id(id: int = Path(...)):
    # Get the user with the specified ID from the database
    # ...

    # Return the user
    return user

@app.put("/users/{id}", response_model=User)
async def update_user(id: int = Path(...), user: User = Body(...)):
    # Update the user with the specified ID in the database
    # ...

    # Return the updated user
    return user

@app.delete("/users/{id}", response_model=None)
async def delete_user(id: int = Path(...)):
    # Delete the user with the specified ID from the database
    # ...

