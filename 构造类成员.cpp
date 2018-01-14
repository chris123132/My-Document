#include "stdafx.h"
#include <iostream>
#include <string.h>
#include <string>
using namespace std;
class StudentID
{
public:
	StudentID(int id)
	{
		value = id;
		cout << "Assingning student id " << value << endl;
	}
	~StudentID()
	{
		cout << "Destructing id " << value << endl;
	}
protected:
	int value;
};

class Student
{
public:
	Student(string& pName, int ssID = 0):id(ssID)
	{
		cout << "Constructing student " << pName << endl;
		name = pName;
	}
protected:
	string name;
	StudentID id;
};

int main()
{
	string ss("Randy");
	Student s(ss, 9818);
	return 0;
}