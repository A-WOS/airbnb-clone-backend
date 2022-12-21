from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
        "title": "Hello! this title comes from django!",
    }
    return render(request, "all_rooms.html", context)


def see_one_room(request, room_id):
    # room = Room.objects.get(pk=room_id)
    room = get_object_or_404(Room, pk=room_id)
    context = {
        "room": room,
    }
    return render(request, "room_detail.html", context)
