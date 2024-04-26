# ----------------------------

class XEvent:

    def __init__(self) -> None:
        class _events_list:
            def __init__(self) -> None:
                self.name = ""
                self.function = 0

        self._events_list = []
        self.debug = 0

    def logging(self, level) -> None:
        self.debug = level

    def show_info(self, text) -> None:
        if(self.debug):
            print(f'{text}')

    def find_event(self, _search) -> int:
        for idx, _ev in enumerate(self._events_list):
            if _ev[0] == _search:
                return idx
        return -1
    
    def add_event(self, event_name, target_function) -> object:
        if(self.find_event(event_name) == -1):
            self._events_list.append([event_name, target_function])
            self.show_info(f"XEvent SUCCSESS: The event '{event_name}' was successfully added")
        else:
            self.show_info(f"XEvent Warning: The event '{event_name}' is already created")
        return self
    
    def del_event(self, event_name) -> object:
        event_to_delete = self.find_event(event_name)
        if(event_to_delete == -1):
            self.show_info(f"XEvent ERROR: The event '{event_name}' can't be deleted, it is not in the event list")
        else:
            try:
                self._events_list.pop(event_to_delete)
                self.show_info(f"XEvent SUCCSESS: The event '{event_name}' is deleted")
            except:
                self.show_info(f"XEvent ERROR: Unknown error when deleting '{event_name}'")
        return self

    def call_event(self, event_name, *target_function_args):
        result = None
        event_to_call = self.find_event(event_name)
        if(event_to_call == -1):
            self.show_info(f"XEvent ERROR: The event '{event_name}' can't be called, it is not in the event list")
        else:
            try:
                result = self._events_list[event_to_call][1](*target_function_args)
                self.show_info(f"XEvent SUCCSESS: The event '{event_name}' called successfully")
            except:
                self.show_info(f"XEvent ERROR: Unknown error when calling '{event_name}'")
        return result
    
    def list_events(self) -> list:
        result = []
        for _ev in self._events_list:
            result.append(_ev[0])
        return result

xevents = XEvent()
xevents.logging(1)