import sys
import logging
from decorators import *
import ipaddress


class Port:
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not (1024 <= value <= 65535):
            instance.logger.critical(
                f'Попытка запуска с указанием неподходящего порта {value}.'
                f' Допустимы адреса с 1024 до 65535.')
            exit(1)
        setattr(instance, self.name, value)
        
class Addr():
    __slots__ = ('name',)
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
       
    def __set__(self, instance, value):
        if value:
            try:
                ip = ipaddress.ip_address(value)
                print(ip)
            except ValueError as e:
                instance.logger.critical(f'Неправильно введён ip-адресс {e}')
                exit(1)
        setattr(instance, self.name, value)
    
    

