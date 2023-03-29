select e.name as Employee
from e.employer inner join m.employer
on e.manager_id = m.id
where e.salary > m.salary