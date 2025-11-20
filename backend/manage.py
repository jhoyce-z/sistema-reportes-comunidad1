#!/usr/bin/env python 
import os 
import sys 
 
def main(): 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'community_project.settings') 
    try: 
        from django.core.management import execute_from_command_line 
    except ImportError: 
        print("Error: Django no está instalado.") 
        return 
    execute_from_command_line(sys.argv) 
 
if __name__ == '__main__': 
    main() 
