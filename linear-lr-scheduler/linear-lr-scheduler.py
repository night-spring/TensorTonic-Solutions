def linear_lr(step, total_step, initial_lr, final_lr=0.0, warmup_step=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    step are 0-based; clamp at final_lr after total_step.
    """
    # Write code here
    if step < warmup_step:
        return step * initial_lr / warmup_step
    elif warmup_step <= step <= total_step:
        return final_lr - (final_lr - initial_lr) * ((total_step - step) / max(1, (total_step - warmup_step)))
    else:
        return final_lr