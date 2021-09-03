subscribers=dict()


def subscribe(event,fn):
    if not event in subscribers:
        subscribers[event]=[]
    subscribe[event].append(fn)

def post_event(event,data):
    if not event in subscribers:
        return
    for fn in subscribe[event]:
        fn(data)            
