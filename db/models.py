# models_sindicacion.py
# Fecha de creación: 2025-07-15  
# Modelado de datos conforme al esquema del feed de sindicación ATOM de PLACE (ContractFolderStatus y relacionados)
# Dependencias: catálogos definidos en archivos .gc y entidades comunes (Party, Address, etc.)

from sqlalchemy import Column, String, Integer, Date, Time, Text, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ContractFolderStatus(Base):
    __tablename__ = "contract_folder_status"

    uuid = Column(String, primary_key=True)
    id = Column(String, nullable=False)
    contract_folder_id = Column(String, nullable=False)
    issue_date = Column(Date)
    issue_time = Column(Time)
    description = Column(Text)

    contracting_party_id = Column(ForeignKey("contracting_party.id"))
    contracting_party = relationship("ContractingParty")

    tendering_process_id = Column(ForeignKey("tendering_process.id"))
    tendering_process = relationship("TenderingProcess")

    tendering_terms_id = Column(ForeignKey("tendering_terms.id"))
    tendering_terms = relationship("TenderingTerms")

    signature_id = Column(ForeignKey("signature.id"))
    signature = relationship("Signature")

    lots = relationship("ProcurementProjectLot", back_populates="contract")
    tender_results = relationship("TenderResult", back_populates="contract")


class ContractingParty(Base):
    __tablename__ = "contracting_party"

    id = Column(String, primary_key=True)
    name = Column(String)
    party_identification = Column(String)
    postal_address = Column(String)
    contact_info = Column(String)


class TenderingProcess(Base):
    __tablename__ = "tendering_process"

    id = Column(String, primary_key=True)
    procedure_code = Column(String, ForeignKey("procedure_code.code"))
    urgency_code = Column(String, ForeignKey("urgency_code.code"))
    submission_method_code = Column(String)


class TenderingTerms(Base):
    __tablename__ = "tendering_terms"

    id = Column(String, primary_key=True)
    awarding_method_type_code = Column(String)
    price_evaluation_code = Column(String)
    maximum_variant_quantity = Column(Integer)
    document_reference_id = Column(ForeignKey("document_reference.id"))
    document_reference = relationship("DocumentReference")


class DocumentReference(Base):
    __tablename__ = "document_reference"

    id = Column(String, primary_key=True)
    document_type = Column(String)
    document_description = Column(Text)
    attachment_uri = Column(String)


class Signature(Base):
    __tablename__ = "signature"

    id = Column(String, primary_key=True)
    signatory_party_id = Column(ForeignKey("contracting_party.id"))
    signatory_party = relationship("ContractingParty")
    digital_signature_attachment = Column(Text)


class ProcurementProjectLot(Base):
    __tablename__ = "procurement_project_lot"

    id = Column(String, primary_key=True)
    contract_id = Column(ForeignKey("contract_folder_status.uuid"))
    contract = relationship("ContractFolderStatus", back_populates="lots")
    description = Column(Text)


class EconomicOperatorParty(Base):
    __tablename__ = "economic_operator_party"

    id = Column(String, primary_key=True)
    party_name = Column(String)
    party_identification = Column(String)
    postal_address = Column(String)
    contact_info = Column(String)


class TenderResult(Base):
    __tablename__ = "tender_result"

    id = Column(String, primary_key=True)
    contract_id = Column(ForeignKey("contract_folder_status.uuid"))
    contract = relationship("ContractFolderStatus", back_populates="tender_results")

    result_code = Column(String, ForeignKey("award_status_code.code"))
    award_date = Column(Date)
    received_tender_quantity = Column(Integer)

    economic_operator_party_id = Column(ForeignKey("economic_operator_party.id"))
    economic_operator_party = relationship("EconomicOperatorParty")

    lot_id = Column(ForeignKey("procurement_project_lot.id"))
    lot = relationship("ProcurementProjectLot")


# Catálogos referenciados

class ProcedureCode(Base):
    __tablename__ = "procedure_code"
    code = Column(String, primary_key=True)
    description = Column(String, nullable=False)

class UrgencyCode(Base):
    __tablename__ = "urgency_code"
    code = Column(String, primary_key=True)
    description = Column(String, nullable=False)

class AwardStatusCode(Base):
    __tablename__ = "award_status_code"
    code = Column(String, primary_key=True)
    description = Column(String, nullable=False)

