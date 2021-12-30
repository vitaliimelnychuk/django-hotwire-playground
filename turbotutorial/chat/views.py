from django.shortcuts import render, reverse, get_object_or_404

from django.views.generic import CreateView, ListView, DetailView

from chat.models import Room, Message


class RoomList(ListView):
    model = Room
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = Room
    context_object_name = "room"

class TurboTest(DetailView):
    model = Message
    fields = ["text"]
    template_name = "chat/components/message_create.html"

# class MessageCreate(CreateView):
#     model = Message
#     fields = ["text"]
#     template_name = "chat/components/message_create.html"

#     def get_success_url(self):
#         # Redirect to the empty form
#         return reverse("send", kwargs={"pk": self.kwargs["pk"]})

#     def form_valid(self, form):
#         room = get_object_or_404(Room, pk=self.kwargs["pk"])
#         form.instance.room = room
#         return super().form_valid(form)
