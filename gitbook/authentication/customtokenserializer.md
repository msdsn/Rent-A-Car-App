# ✂️ CustomTokenSerializer

{% code title="users/serializers.py" %}
```python
# ... [importlar]
from dj_rest_auth.serializers import TokenSerializer

# ...

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
```
{% endcode %}
