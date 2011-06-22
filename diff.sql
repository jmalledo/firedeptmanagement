ALTER TABLE "personal_firefigther" ADD COLUMN "user_id" integer UNIQUE REFERENCES "auth_user" ("id");
