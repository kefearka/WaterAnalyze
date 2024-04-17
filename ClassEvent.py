class XEvent:

    def __init__(self, dbg) -> None:
        class _events_list:
            def __init__(self) -> None:
                self.name = ""
                self.function = 0

        self._events_list = []
        self.debug = dbg

    def show_info(self, text):
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

xevents = XEvent(1)


# class old_Event():
#     def push(self, event_name, target_function, target_function_args_num):
#         if event_name not in self.handle:
#             self.handle += [target_function_args_num + 2, event_name, target_function]
#             print(f"XEvent Success: The event '{event_name}' was successfully added")
#         else:
#             print(f"XEvent Warning: The event '{event_name}' is already created")
#         return self

#     def pop(self, event_name):
#         try:
#             index = self.handle.index(event_name)
#             for idx in range(0, 3):
#                 self.handle.pop(idx)
#             print(f"XEvent Success: The event '{event_name}' is deleted")
#         except ValueError:
#             print(f"XEvent ERROR: The event '{event_name}' can't be deleted, it is not in the event list")
#         return self

#     def jmp(self, event_name, target_function_args=None):
#         try:
#             index = self.handle.index(event_name)
#             # self.handle[index + 1]() if (self.handle[index + 2] == None) else self.handle[index + 1](self.handle[index + 2])
#             if (self.handle[index - 1] == 2):
#                 self.handle[index + 1]()
#                 return self
#             if(self.handle[index - 1] != len(target_function_args) + 2):
#                 print(f"XEvent ERROR: Incorrect number of arguments for '{event_name}' event")
#                 return self
#             else:
#                 self.handle[index + 1](*target_function_args)
#         except ValueError:
#             print(f"XEvent ERROR: The event '{event_name}' can't be complited, it is not in the event list")
#             return self
#         except:
#             print(f"XEvent ERROR: Unknown error when calling '{event_name}'")
#             return self

#         print(f"XEvent SUCCESS: The event '{event_name}' has been completed")
#         return self
    
# class Event:

#     def __init__(self) -> None:
#         self.handle = []

#     def push(self, event_name, target_function, target_function_args):
#         if event_name not in self.handle:
#             self.handle += [event_name, target_function, target_function_args]
#             print(f"Event Success: The event '{event_name}' was successfully added")
#         else:
#             print(f"Event Warning: The event '{event_name}' is already created")
#         return self

#     def pop(self, event_name):
#         try:
#             index = self.handle.index(event_name)
#             self.handle.pop(index)
#             self.handle.pop(index + 1)
#             self.handle.pop(index + 2)
#             print(f"Event Success: The event '{event_name}' is deleted")
#         except ValueError:
#             print(f"Event ERROR: The event '{event_name}' can't be deleted, it is not in the event list")
#         return self

#     def jmp(self, event_name):
#         error = 0
#         try:
#             index = self.handle.index(event_name)
#             self.handle[index + 1]() if (self.handle[index + 2] == None) else self.handle[index + 1](self.handle[index + 2])
#         except ValueError:
#             print(f"Event ERROR: The event '{event_name}' can't be complited, it is not in the event list")
#             error = 1
#         except:
#             print(f"Event ERROR: Unknown error when calling '{event_name}'")
#             error = 1
#         finally:
#             if not error:
#                 print(f"Event SUCCESS: The event '{event_name}' has been completed")
#         return self


# events = Event()
# -----------------------

# class XEvent:

#     def __init__(self, dbg) -> None:
#         class _events_list:
#             def __init__(self) -> None:
#                 self.name = ""
#                 self.function = 0
#                 # self.function_args_num = None

#         self._events_list = []
#         self.debug = dbg

#     def show_info(self, text):
#         if(self.debug):
#             print(f'{text}')

#     def find_event(self, _search) -> int:
#         for idx, _ev in enumerate(self._events_list):
#             if _ev[0] == _search:
#                 return idx
#         return -1

#     '''Старый метод, учитывающий количество аргументов'''
#     def add_event(self, event_name, target_function, target_function_args_num) -> object:
#         if(self.find_event(event_name) == -1):
#             self._events_list.append([event_name, target_function, target_function_args_num])
#             print(f"XEvent SUCCSESS: The event '{event_name}' was successfully added")
#         else:
#             print(f"XEvent Warning: The event '{event_name}' is already created")
#         return self
       
#     def del_event(self, event_name) -> object:
#         event_to_delete = self.find_event(event_name)
#         if(event_to_delete == -1):
#             self.show_info(f"XEvent ERROR: The event '{event_name}' can't be deleted, it is not in the event list")
#         else:
#             try:
#                 self._events_list.pop(event_to_delete)
#                 self.show_info(f"XEvent SUCCSESS: The event '{event_name}' is deleted")
#             except:
#                 self.show_info(f"XEvent ERROR: Unknown error when deleting '{event_name}'")
#         return self
    
#     '''Старый метод, учитывающий количество аргументов'''
#     def call_event(self, event_name, *target_function_args) -> object:
#         event_to_call = self.find_event(event_name)
#         if(event_to_call == -1):
#             print(f"XEvent ERROR: The event '{event_name}' can't be called, it is not in the event list")
#         else:
#             if(self._events_list[event_to_call][2] != len(target_function_args)):
#                 print(f"XEvent ERROR: Incorrect number of arguments for '{event_name}' event")
#             else:
#                 try:
#                     self._events_list[event_to_call][1](*target_function_args)
#                     print(f"XEvent SUCCSESS: The event '{event_name}' called successfully")
#                 except:
#                     print(f"XEvent ERROR: Unknown error when calling '{event_name}'")
#         return self
    
#     def list_events(self) -> list:
#         result = []
#         for _ev in self._events_list:
#             result.append(_ev[0])
#         return result

# xevents = XEvent(0)

#####TEST#####

# def f1(arg1, arg2, arg3):
#     print(arg1+arg2+arg3)

# def f2():
#     print("f2!!")

# def f3(arg1, arg2):
#     print(arg1, arg2)
#     print("wrong arguments!!!!")

# xevents.add_event("Function 1", f1, 3)
# xevents.add_event("Function 2", f2, 0)
# xevents.add_event("Function 3, wrong argument", f3, 2)

# xevents.del_event("try to delete empty event")

# xevents.call_event("Function 1", 1,2,3)
# xevents.call_event("Function 2")
# xevents.call_event("Function 3, wrong argument", 1,2,3)

# xevents.del_event("Function 2")
# print("function 2 is deleted")

# xevents.call_event("Function 1", 1,2,3)
# xevents.call_event("Function 2")
# xevents.call_event("Function 3, wrong argument", 1,2)

# print(xevents.list_events())