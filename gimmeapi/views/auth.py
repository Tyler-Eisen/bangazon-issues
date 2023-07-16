from rest_framework.decorators import api_view
from rest_framework.response import Response
from gimmeapi.models.user import User

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']
 # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()
 # If authentication was successful, respond with their token
    if user is not None:
        data = {
          'id':user.id,
          'uid': user.uid,
          'email': user.email,
          'address': user.address,
          'phone': user.phone,
          'image_url':user.image_url
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the rareapi_user table
    user = User.objects.create(
      uid = request.data['uid'],
      email = request.data['email'],
      address = request.data['address'],
      phone = request.data['phone'],
      image_url = request.data['imageUrl'],
    )

# Return the user info to the client
    data = {
      'id': user.id,
      'uid': user.uid,
      'email': user.email,
      'address': user.address,
      'phone' : user.phone,
      'image_url' : user.image_url   
    }
    return Response(data)
