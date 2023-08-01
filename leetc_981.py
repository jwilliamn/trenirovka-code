#!/usr/bin/env python
# coding: utf-8

# Leet Code problem: 981


class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data:
            self.data = {key:{'val':[value],
                         'time':[timestamp]}}

        if key not in self.data:
            self.data[key] = {'val':[value],
                         'time':[timestamp]}
        else:
            self.data[key]['val'].append(value)
            self.data[key]['time'].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        #print(self.data)
        if key not in self.data:
            return ""
        else:
            times = self.data[key]['time']
            values = self.data[key]['val']

            l = 0
            r = len(times) - 1
            target = timestamp

            if target < times[l]:
                return ""

            while l <= r:
                mid = (l + r)//2
                if times[mid] == target:
                    return values[mid]
                elif target > times[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if target < times[mid]:
                mid = mid - 1
            return values[mid]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

    