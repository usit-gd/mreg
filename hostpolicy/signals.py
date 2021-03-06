from django.db.models.signals import m2m_changed, pre_delete, pre_save
from django.dispatch import receiver

from .models import HostPolicyAtom, HostPolicyRole


@receiver(m2m_changed, sender=HostPolicyRole.atoms.through)
@receiver(m2m_changed, sender=HostPolicyRole.hosts.through)
def role_update_updated_at_on_changes(sender, instance, action, model,
                                      reverse, pk_set, **kwargs):
    """
    Update the hostpolicyrole updated_at field whenever its atoms, hosts or
    parent  m2m relations have successfully been altered.
    """
    if action in ('post_add', 'post_remove', 'post_clear',):
        instance.save()


def _hostpolicyatom_update_m2m_relations(instance):
    for role in instance.roles.all():
        role.save()


@receiver(pre_save, sender=HostPolicyAtom)
def atom_update_m2m_relations_on_rename(sender, instance, raw, using, update_fields, **kwargs):
    """
    Update hostgroup and hostpolicy on host rename
    """
    # Ignore newly created hosts
    if not instance.id:
        return

    oldname = HostPolicyAtom.objects.get(id=instance.id).name
    if oldname != instance.name:
        _hostpolicyatom_update_m2m_relations(instance)


@receiver(pre_delete, sender=HostPolicyAtom)
def atom_update_m2m_relations_on_delete(sender, instance, using, **kwargs):
    """
    No signal is sent for m2m relations on delete, so use a pre_delete on
    HostPolicyAtom instead.
    """
    _hostpolicyatom_update_m2m_relations(instance)
