Employee updatedEmployee = context.Employees.Where(x => x.EmployeeID == ef.First.EmployeeID).First();
Assert.AreEqual(result.EmployeeID, updatedEmployee.EmployeeID);
Assert.AreEqual(testEmployee.Active, updatedEmployee.Active);
Assert.AreEqual(testEmployee.Email, updatedEmployee.Email);
Assert.AreEqual(testEmployee.FirstName, updatedEmployee.FirstName);
Assert.AreEqual(testEmployee.LastName, updatedEmployee.LastName);
Assert.AreEqual(testEmployee.LoginName, updatedEmployee.LoginName);
Assert.AreEqual(testEmployee.Phone, updatedEmployee.Phone);

/*
Employee updatedEmployee = context.Employees.Where(x => x.EmployeeID == ef.First.EmployeeID).First();
Assert.AreEqual(result.EmployeeID, updatedEmployee.EmployeeID);
Assert.AreEqual(testEmployee.Active, updatedEmployee.Active);
Assert.AreEqual(testEmployee.Email, updatedEmployee.Email);
Assert.AreEqual(testEmployee.FirstName, updatedEmployee.FirstName);
Assert.AreEqual(testEmployee.LastName, updatedEmployee.LastName);
Assert.AreEqual(testEmployee.LoginName, updatedEmployee.LoginName);
Assert.AreEqual(testEmployee.Phone, updatedEmployee.Phone);
Assert.AreNotEqual(ef.First.UpdatedOn, updatedEmployee.UpdatedOn);
Assert.AreEqual(testEmployee.LookupEmployeeRoleId, updatedEmployee.LookupEmployeeRoleId);

*/