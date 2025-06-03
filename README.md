A **Counterparty Improvement Proposal** is a formal proposal relating to a change in the Counterparty Protocol. This document describes the process for proposing and ratifying CIPs. All Counterparty protocol changes should be published, discussed and decided in the form of a CIP; however, CIPs should not be created unnecessarily: neither for "informational" purposes, nor for non-protocol changes to the [Counterparty Core](https://github.com/CounterpartyXCP/counterparty-core/) reference implementation. Counterparty Core is [open-source and freely licensed](https://github.com/CounterpartyXCP/counterparty-core/LICENSE), and users are free to fork the repository as desired.

For documentation as to the design and use of Counterparty, please refer to the [official Counterparty Documentation](https://docs.counterparty.io/docs/basics/what-is-counterparty/) and [Whitepaper](https://krellenstein.com/adam/get/counterparty-whitepaper_2024-04-25.pdf). For general discussion about the Counterparty protocol, ecosystem, reference implementation or other related projects, please use the [Counterparty Discussion Forums](https://github.com/CounterpartyXCP/Forum/discussions). For reporting bugs, discussing particular implementation details, or proposing changes to Counterparty Core that are not consensus-critical, please see the [Counterparty Core Issue Tracker](https://github.com/CounterpartyXCP/counterparty-core/issues).


## CIP Format ##

A CIP should provide a concise technical specification of the change to the Counterparty Protocol and a rationale for making the change. CIPs should be written in Markdown format and stored in this Git repository; the revision history is the historical record of the proposal.

Each CIP should have the following parts:

* Preamble -- RFC 822-style headers containing metadata about the CIP, including the CIP number, a short descriptive title, the names, and optionally the contact info for each author, etc.

* Abstract -- A short (~200 word) description of the technical issue being addressed.

* Copyright -- Each CIP must either be explicitly placed in the public domain or licensed under the Open Publication License.

* Specification -- The technical specification should describe the syntax and semantics of any new feature. The specification should be detailed enough to allow for competing independent implementations of the Counterparty Protocol.

* Motivation -- The motivation should clearly explain why the existing protocol specification is inadequate to address the problem that the CIP solves.

* Rationale -- The rationale fleshes out the specification by describing what motivated the design and why particular design decisions were made. It should describe alternate designs that were considered and related work, including important objections or concerns raised during previous discussions.

* Backwards Compatibility -- All CIPs that introduce backwards incompatibilities must include a section describing these incompatibilities and their significance. The CIP must explain how the author proposes to deal with these incompatibilities.

* Reference Implementation -- The reference implementation must be completed before any CIP is given status "Final", but it need not be completed before the CIP is accepted.


## CIP Lifecycle ##

CIPs may be edited and managed by any Counterparty maintainer, where a maintainer is any individual that has commit access to the Counterparty Core repository and has made at least one commit in the previous nine-month period. 

CIPs should be created as pull requests to this repository. These pull requests may be merged / rejected, and their status changed, by any Counterparty maintainer. CIPs may be rejected for a number of reasons, including failing to adhere to the above CIP format, being insufficiently motivated / documented, being unfocused, vague or ambiguous, being technically infeasible, etc. For a CIP to be accepted it must meet certain minimum criteria. It must be a clear and complete description of the proposed enhancement. The enhancement must represent a net improvement. The proposed implementation, if applicable, must be solid and must not complicate the protocol unduly.

To be accepted, the CIP's pull request must be approved ("ACKed") by a simple majority of Counterparty maintainers. If there is only one maintainer, only his or her ACK is necessary.

Once a CIP has been accepted, its status should formally be set to "Accepted" and its reference implementation must be completed. When the reference implementation is complete and merged into the `master` branch of the Counterparty Core repository, the status should be changed to "Final".

A CIP in "Draft" status can also be assigned a status of "Deferred". The CIP author or, or any maintainer, can assign the CIP this status when no progress is being made on the CIP. Once a CIP is "Deferred", a Counterparty maintainer can re-assign it to "Draft" status at will.

A CIP can also be "Rejected". Perhaps after all is said and done it was not a good idea. It is still important to have a record of this fact.

CIPs can be superseded by a different CIP, rendering the original obsolete.

The possible paths of the status of CIPs are as follows:

<img src=process.png></img>


## CIP History ##

In this repository there resides an [archive](cip-archive/) of pre-2025 CIPs, which were important in the context of the history of Counterparty and its ecosystem but largely independent of Counterparty development. While [over 30 CIPs](cip-archive/README.md) were created between 2015 and 2023, only a few were ever ratified, and those were purely informational / process-oriented. All historical CIPs should be considered abandoned in their current form, but of course they may be re-submitted (assuming they meet the current standards). CIP indexing will commence with CIP-34 to avoid confusion.
