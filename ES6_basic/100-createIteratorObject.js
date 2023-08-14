export default function createIteratorObject(report) {
  const employeesByDepartment = [];
  for (const value of Object.values(report.allEmployees)) {
    employeesByDepartment.push(...value);
  }
  return employeesByDepartment;
}
