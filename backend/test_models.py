from app.db.models import RefreshToken, User

print(User.__tablename__)
print(RefreshToken.__tablename__)
print(User.refresh_tokens)
