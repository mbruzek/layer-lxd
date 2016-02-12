# Charm Layer for LXD

This repository contains the Charm layer for lxd, which can be used as a
base layer for other Charms that use lxd.  Please refer to the
[Juju composer docs](https://jujucharms.com/docs/devel/authors-charm-composing).

## Usage

In a charm that wants to use lxd, the integration can be as simple as placing
the following in your charm's `layer.yaml`:

    includes: ['layer:lxd']

From here, you simply update any hooks/reactive patterns you require to deliver
and manage the lifecycle of your applications lxd image.

### States

The lxd layer uses the reactive framework to raise a few synthetic events:

- **lxd.installed** - Indicates when lxd is installed. Other layers could
  do things such as configure networking or install additional packages in
  response to this state.

- **lxd.configured** - Indicates that lxd is configured and ready to go.
  Other layers could uset this state to start doing lxc work.

##### lxd.installed

When `lxd.installed` is set, this event is before we signify to other
layers that we are ready to start workloads, which should allow for
lxd extensions to be installed free of disrupting active workloads.

For example, installing a Software Defined Network (SDN) support and getting
the daemon configured for TCP connections.

```python
@when('lxd.installed')
def start_sdn_network():
    # do something here
```

##### lxd.configured

When `lxd.configured` is set, the daemon is considered fully configured
and ready to accept workloads.

```python
@when('lxd.configured')
def start_my_workload():
    # do something with lxd
```

## LXD Information
