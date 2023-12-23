/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/10/25 22:36:46                          */
/*==============================================================*/




/*==============================================================*/
/* Table: Account                                               */
/*==============================================================*/
create table Account
(
   u_no                 char(10) not null  comment '',
   u_state              numeric(1,0)  comment '',
   u_password           varchar(20)  comment '',
   u_type               char(1)  comment '',
   primary key (u_no)
);

/*==============================================================*/
/* Table: AdoptionApplication                                   */
/*==============================================================*/
create table AdoptionApplication
(
   u_name               varchar(10) not null  comment '',
   u_sex                char(1)  comment '',
   u_age                smallint  comment '',
   u_city               varchar(20)  comment '',
   u_phone              numeric(11,0)  comment '',
   u_email              varchar(20)  comment '',
   ap_id                int auto_increment not null  comment '',
   a_id                 int  comment '',
   u_id                 int not null  comment '',
   c_id                 int not null  comment '',
   u_fnum               numeric(2,0)  comment '',
   is_agree             bool  comment '',
   reason               varchar(300)  comment '',
   a_state              char(5)  comment '',
   a_time               datetime  comment '',
   a_result             char(5)  comment '',
   ap_time              datetime  comment '',
   primary key (ap_id)
);

/*==============================================================*/
/* Table: administrator                                         */
/*==============================================================*/
create table administrator
(
   a_id                 int auto_increment not null  comment '',
   u_no                 char(10) not null  comment '',
   primary key (a_id)
);

/*==============================================================*/
/* Table: adopter                                               */
/*==============================================================*/
create table adopter
(
   u_id                 int auto_increment not null  comment '',
   u_no                 char(10) not null  comment '',
   adopt_date           date  comment '',
   adopt_state          char(5)  comment '',
   primary key (u_id)
);

/*==============================================================*/
/* Table: breed                                                 */
/*==============================================================*/
create table breed
(
   b_id                 int auto_increment not null  comment '',
   type_id              int not null  comment '',
   b_name               varchar(20) not null  comment '',
   primary key (b_id)
);

/*==============================================================*/
/* Table: city                                                  */
/*==============================================================*/
create table city
(
   c_id                 int auto_increment not null  comment '',
   c_province           varchar(20) not null  comment '',
   primary key (c_id)
);

/*==============================================================*/
/* Table: pet                                                   */
/*==============================================================*/
create table pet
(
   p_id                 int auto_increment not null  comment '',
   u_id                 int  comment '',
   b_id                 int not null  comment '',
   p_name               varchar(10) not null  comment '',
   p_age                smallint  comment '',
   p_sex                char(1)  comment '',
   p_character          varchar(50)  comment '',
   is_adopted           numeric(1,0) not null  comment '',
   primary key (p_id)
);

/*==============================================================*/
/* Table: traceItem                                             */
/*==============================================================*/
create table traceItem
(
   t_id                 int auto_increment not null  comment '',
   a_id                 int not null  comment '',
   u_id                 int not null  comment '',
   t_date               date  comment '',
   t_situation          varchar(100)  comment '',
   primary key (t_id)
);

/*==============================================================*/
/* Table: type                                                  */
/*==============================================================*/
create table type
(
   type_id              int auto_increment not null  comment '',
   type_name            varchar(5) not null  comment '',
   primary key (type_id)
);

alter table AdoptionApplication add constraint FK_ADOPTION_AUDIT_ADMINIST foreign key (a_id)
      references administrator (a_id) on delete restrict on update restrict;

alter table AdoptionApplication add constraint FK_ADOPTION_APPLICATI_ADOPTER foreign key (u_id)
      references adopter (u_id) on delete restrict on update restrict;

alter table AdoptionApplication add constraint FK_ADOPTION_APPLICATI_CITY foreign key (c_id)
      references city (c_id) on delete restrict on update restrict;

alter table administrator add constraint FK_ADMINIST_USE2_ACCOUNT foreign key (u_no)
      references Account (u_no) on delete restrict on update restrict;

alter table adopter add constraint FK_ADOPTER_USE_ACCOUNT foreign key (u_no)
      references Account (u_no) on delete restrict on update restrict;

alter table breed add constraint FK_BREED_INCLUDE_TYPE foreign key (type_id)
      references type (type_id) on delete restrict on update restrict;

alter table pet add constraint FK_PET_ADOPT_ADOPTER foreign key (u_id)
      references adopter (u_id) on delete restrict on update restrict;

alter table pet add constraint FK_PET_INCLUDE_BREED foreign key (b_id)
      references breed (b_id) on delete restrict on update restrict;

alter table traceItem add constraint FK_TRACEITE_RECORDING_ADMINIST foreign key (a_id)
      references administrator (a_id) on delete restrict on update restrict;

alter table traceItem add constraint FK_TRACEITE_REVISIT_ADOPTER foreign key (u_id)
      references adopter (u_id) on delete restrict on update restrict;

alter table AdoptionApplication 
   drop foreign key FK_ADOPTION_AUDIT_ADMINIST;

alter table AdoptionApplication 
   drop foreign key FK_ADOPTION_APPLICATI_ADOPTER;

alter table AdoptionApplication 
   drop foreign key FK_ADOPTION_APPLICATI_CITY;

alter table administrator 
   drop foreign key FK_ADMINIST_USE2_ACCOUNT;

alter table adopter 
   drop foreign key FK_ADOPTER_USE_ACCOUNT;

alter table breed 
   drop foreign key FK_BREED_INCLUDE_TYPE;

alter table pet 
   drop foreign key FK_PET_ADOPT_ADOPTER;

alter table pet 
   drop foreign key FK_PET_INCLUDE_BREED;

alter table traceItem 
   drop foreign key FK_TRACEITE_RECORDING_ADMINIST;

alter table traceItem 
   drop foreign key FK_TRACEITE_REVISIT_ADOPTER;