"""
git-log-analysis

分析你的git提交日誌。

用法：
  # 獲取待分析log
  git log > xxx.log
  # 把日誌文件放到input文件
  # （最好記得把之前的test給刪掉）
  mv xxx.log input
  # 運行
  python main.py
"""

import os
import re
import datetime


INPUT_LOG_FOLDER_PATH = "input"
ANALYSIS_RESULT_OUTPUT_PATH = "output"

class GitLog:
  def __init__(self, log_str):
    lines = log_str.split('\n')
    self.id = lines[0].strip()
    index = 1
    if lines[index].startswith("Merge:"):
      self.merge = self.__read_line(lines[index], "Merge:")
      index = index + 1
    else:
      self.merge = None
    self.author = self.__read_line(lines[index], "Author:")
    self.date = self.__read_line(lines[index + 1], "Date:")
    self.message = "".join(lines[index + 2 :])
    # Mon Mar 5 09:06:35 2018 +0800
    # %a %b %d %X %Y %z
    # time =  datetime.datetime.strptime(self.date, "%a %b %d %X %Y %z")
    # time_str = time.strftime("%a %b %-d %X %Y %z")
    # if (not (time_str == self.date)):
    #   raise ValueError("error")
    self.date = datetime.datetime.strptime(self.date, "%a %b %d %X %Y %z")

  def __read_line(self, line, header):
    if line.startswith(header):
      return line[len(header):].strip()
    else:
      raise ValueError("{0} not start with {1}".format(line, header))

def load_logs():
  logs = []
  for each_file in os.listdir(INPUT_LOG_FOLDER_PATH):
    if each_file.endswith(".log"):
      each_file_path = "/".join([INPUT_LOG_FOLDER_PATH, each_file])
      with open(each_file_path) as each_log_file :
        file_data = "\n" + each_log_file.read()
        for each_log_str in file_data.split("\ncommit")[1:]:
          each_log = GitLog(each_log_str)
          logs.append(each_log)
  return logs

def day_time_analysis(logs):
  day_time_table = {"common" : 0, "evening": 0, "nignt": 0}
  for log in logs:
    if 8 <= log.date.hour <= 17:
      day_time_table["common"] = day_time_table["common"] + 1
    elif 17 < log.date.hour <= 22:
      day_time_table["evening"] = day_time_table["evening"] + 1
    else:
      day_time_table["nignt"] = day_time_table["nignt"] + 1
  return day_time_table


if __name__ == "__main__":
  # print("git-log-analysis")
  logs = load_logs()
  print(day_time_analysis(logs))
