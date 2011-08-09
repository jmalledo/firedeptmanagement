CREATE TABLE "common_person_childs" (
    "id" integer NOT NULL PRIMARY KEY,
    "person_id" integer NOT NULL,
    "baseperson_id" integer NOT NULL REFERENCES "common_baseperson" ("id"),
    UNIQUE ("person_id", "baseperson_id")
);
 
 
ALTER TABLE "common_person" ADD COLUMN "civil_state" varchar(1);
                                                                                                                                                         