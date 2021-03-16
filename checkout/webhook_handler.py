from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handle generic/unknown/unexpected webhook """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ handle payment_intent.succeeded webhook from stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ handle payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
