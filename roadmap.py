!pip install roadmapper
!pip install --upgrade roadmapper

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

roadmap = Roadmap(1200, 400, colour_theme="BLUEMOUNTAIN")
roadmap.set_title("ROADMAP FOR CAREER IN CODING")
choice=input("ENTER A PROGRAMMING LANGUAGE::")
response=input("DO YOU KNOW BASICS (enter YES or NO):")

if choice.upper()=="PYTHON":
    if response.upper()=="NO":
        roadmap.set_subtitle("PYTHON")
        roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=12)
        roadmap.add_logo("E:\\Outputs\\samplep.png", "top-right", 50,50)

        group = roadmap.add_group("TIME DURATION(IN MONTHS)-----> \n \n REFERENCE SOURCE----->")

        task = group.add_task("LEARNING PROCESS", "2024-01-01", "2024-08-31")
        task.add_milestone("BASICS", "2024-03-31")
        task.add_milestone("ADVANCE", "2024-08-31")
        parellel_task = task.add_parallel_task("MINI PROJECT", "2024-11-01", "2024-12-31")
        parellel_task.add_milestone("TEST ON BASICS", "2024-04-30")
        parellel_task.add_milestone("TEST ON ADVANCE", "2024-09-30")

        task = group.add_task("GEEKS FOR GEEKS", "2024-01-01", "2024-03-31")
        task.add_parallel_task("CODECADEMY", "2024-05-01", "2024-08-31")

        roadmap.set_footer("KEEP LEARNING...\n ALL THE BEST...")
        roadmap.draw()
        roadmap.save("E:\\pythonproject\\PYTHONNO.png")
    else:
        roadmap.set_subtitle("PYTHON")
        roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=12)
        roadmap.add_logo("E:\\Outputs\\samplep.png", "top-right", 50,50)

        group = roadmap.add_group("TIME DURATION(IN MONTHS)-----> \n \n REFERENCE SOURCE----->")

        task = group.add_task("LEARNING PROCESS", "2024-01-01", "2024-08-31")
        task.add_milestone("BASICS", "2024-01-31")
        task.add_milestone("ADVANCE", "2024-08-31")
        parellel_task = task.add_parallel_task("WORK ON PROJECT", "2024-10-01", "2024-12-31")
        parellel_task.add_milestone("TEST ON ADVANCE", "2024-09-30")

        task = group.add_task("GEEKS FOR GEEKS", "2024-01-01", "2024-01-31")
        task.add_parallel_task("COURSERA", "2024-02-01", "2024-08-31")

        roadmap.set_footer("KEEP LEARNING...\n ALL THE BEST...")
        roadmap.draw()
        roadmap.save("E:\\pythonproject\\PYTHONYES.png")
  
    
    
elif choice.upper()=="C":
    if response.upper()=="NO":
        roadmap.set_subtitle("C PROGRAMMING")
        roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=12)
        roadmap.add_logo("E:\\Outputs\\samplec.png", "top-right", 50,50)

        group = roadmap.add_group("TIME DURATION(IN MONTHS)-----> \n \n REFERENCE SOURCE----->")

        task = group.add_task("LEARNING PROCESS", "2024-01-01", "2024-08-31")
        task.add_milestone("BASICS", "2024-03-31")
        task.add_milestone("ADVANCE", "2024-08-31")
        parellel_task = task.add_parallel_task("MINI PROJECT", "2024-11-01", "2024-12-31")
        parellel_task.add_milestone("TEST ON BASICS", "2024-04-30")
        parellel_task.add_milestone("TEST ON ADVANCE", "2024-09-30")

        task = group.add_task("C TUTORIAL", "2024-01-01", "2024-03-31")
        task.add_parallel_task("UDEMY", "2024-05-01", "2024-08-31")

        roadmap.set_footer("KEEP LEARNING...\n ALL THE BEST...")
        roadmap.draw()
        roadmap.save("E:\\pythonproject\\C-NO.png")
    else:
        roadmap.set_subtitle("C PROGRAMMING")
        roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=12)
        roadmap.add_logo("E:\\Outputs\\samplec.png", "top-right", 50,50)

        group = roadmap.add_group("TIME DURATION(IN MONTHS)-----> \n \n REFERENCE SOURCE----->")

        task = group.add_task("LEARNING PROCESS", "2024-01-01", "2024-08-31")
        task.add_milestone("BASICS", "2024-01-31")
        task.add_milestone("ADVANCE", "2024-08-31")
        parellel_task = task.add_parallel_task("WORK ON PROJECT", "2024-10-01", "2024-12-31")
        parellel_task.add_milestone("TEST ON ADVANCE", "2024-09-30")

        task = group.add_task("C TUTORIAL", "2024-01-01", "2024-01-31")
        task.add_parallel_task("COURSERA", "2024-02-01", "2024-08-31")

        roadmap.set_footer("KEEP LEARNING...\n ALL THE BEST...")
        roadmap.draw()
        roadmap.save("E:\\pythonproject\\C-YES.png")
  
    
else:
    print("STILL IMPLEMENTING.......!")
    
print("THANK YOU , HAVE A NICE DAY.")


