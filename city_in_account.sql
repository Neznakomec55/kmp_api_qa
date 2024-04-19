from sqlalchemy import create_engine
from sqlalchemy.orm import Session

SELECT
	keyauto.account_user.id,
	password,
	last_login,
	first_name,
	last_name,
	email,
	keyauto.account_user.created,
	keyauto.account_user.modified,
	keyauto.account_user.eid,
	validated,
	birthday,
	consent,
	keyauto.account_user.name,
	send_service_push,
	deletion_date,
	keyauto.reference_city.id,
	keyauto.reference_city.name
FROM
	keyauto.account_user
	LEFT JOIN keyauto.reference_city ON keyauto.account_user.city_id = keyauto.reference_city.id;