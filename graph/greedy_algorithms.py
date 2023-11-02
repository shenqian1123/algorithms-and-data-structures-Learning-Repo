## greedy algor


## 创建会议数据类型
class Meeting:

    def __init__(self, start, end):
        self.start = start 
        self.end = end

    def __lt__(self, m1):
        return self.end < m1.end
    

## 创建安排会议的处理类
class MeetingArrange:
    
    def __init__(self, m_list):
        self.meets = self.list2meets(m_list)
    
    def list2meets(self, m_list):
        meets_list = []
        for m in m_list:
            meets_list.append(Meeting(m[0], m[1]))
        return meets_list

    def meets2list(self, meets):
        m_list = []
        for meet in meets:
            m_list.append([meet.start, meet.end])
        return m_list

    def run(self):
        # 使用sort方法对meets进行排序
        self.meets = sorted(self.meets)
        # print(self.meets2list(self.meets))
        cur_begin_time = 0
        result = 0
        for m in self.meets:
            if m.start >= cur_begin_time:
                result = result + 1
                cur_begin_time = m.end

        print(result)
        


## 1.找到一天可以安排最多场会议的安排
def best_arange(meeting_list):

    ## conver list to dict 
    ## list : valid, pincked, unvalid
    meeting_dict = {}
    meeting_dict["valid"] = []
    meeting_dict["min"] = []
    meeting_dict["disabled"] = []
    for meeting in meeting_list:
        meeting_dict["valid"].append(meeting)

    while (not get_meeting_valid_exist(meeting_dict)):
        ## 遍历一轮，找到最早结束的会议
        ## 最早结束的会议标记为picked
        ## 在valid状态的会议中找出开始时间早于min结束时间的会议，标记为unvalid
        meeting_dict = marked_min_end_meeting(meeting_dict)
        meeting_dict = disable_meeting_begin_before_min(meeting_dict)
        print(meeting_dict)
    
    return meeting_dict


## 判断字典中是否还有valid的会议
## valid表示该会议还没有被处理
def get_meeting_valid_exist(m_dict):
    return m_dict["valid"] == []

## 将字典中结束时间最早的会议标记为min, 并返回
def marked_min_end_meeting(m_dict):
    min_end_time = float("inf")
    min_end_meeting = None

    for m in m_dict["valid"]:
        if m[1] < min_end_time:
            min_end_time = m[1]
            min_end_meeting = m
    m_dict["valid"].remove(min_end_meeting)
    m_dict["min"].append(min_end_meeting)
    return m_dict

## 返回结束时间最早的会议
def get_min_end_meeting(m_dict):
    return m_dict["min"][-1]

## 将字典中开始时间早于被标记为min会议的结束时间的会议disable
def disable_meeting_begin_before_min(m_dict):
    for m in m_dict["valid"]:
        if m[0] > get_min_end_meeting(m_dict)[1]:
            m_dict["valid"].remove(m)
            m_dict["disabled"].append(m)
    return m_dict



if __name__ == "__main__":
    test_meeting = [[1, 2], [3, 6], [4, 10], [9, 11], [4, 6], [5, 8], [6, 9]]
    print(best_arange(test_meeting))
    MeetingArrange(test_meeting).run()
